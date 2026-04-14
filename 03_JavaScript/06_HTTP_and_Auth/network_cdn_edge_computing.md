## 1. 개념 정의

### **CDN (Content Delivery Network)**
전 세계 여러 지역에 물리적으로 분산된 서버 네트워크를 통해, 사용자에게 웹 콘텐츠(이미지, JS, CSS 등)를 가장 **가까운 곳에서 빠르게 전달**하는 시스템이다.

* **Origin Server (원본 서버)**: 콘텐츠가 처음 저장되는 중앙 서버이다.
* **Edge Server (엣지 서버/캐시 서버)**: 전 세계 곳곳(PoP, Points of Presence)에 배치되어 원본 서버의 복사본을 저장하고 사용자에게 직접 데이터를 전달하는 서버이다.

---

## 2. 작동 방식 및 효과

| 구분 | 내용 | 기대 효과 |
| :--- | :--- | :--- |
| **캐싱 (Caching)** | 자주 요청되는 정적 파일을 엣지 서버에 미리 복사하여 저장함 | 원본 서버의 부하를 획기적으로 줄임 |
| **라우팅 (Routing)** | 사용자의 IP 주소를 분석해 가장 지연 시간이 짧은 엣지 서버로 연결 | 데이터 전송 거리 단축으로 로딩 속도 향상 |
| **부하 분산** | 트래픽이 여러 엣지 서버로 분산되어 처리됨 | 대규모 접속 시에도 서비스 안정성 유지 |
| **가용성** | 특정 서버에 장애가 발생해도 인접한 다른 서버가 대신 응답 | 서비스 중단 위험 최소화 (고가용성) |

---

## 3. 심화 개념 보강: 프론트엔드 관점의 활용

### **① 정적 에셋(Static Assets)의 전송**
프론트엔드 빌드 결과물인 `bundle.js`, `style.css`, 그리고 각종 이미지 파일들을 CDN을 통해 배포한다. 특히 용량이 큰 라이브러리나 고해상도 이미지를 처리할 때 필수적이다.

### **② 캐시 무효화 (Cache Invalidation)**
코드를 수정하여 새로 배포했을 때, 엣지 서버에 남아있는 옛날 파일(캐시) 때문에 사용자가 업데이트된 내용을 못 볼 수 있다. 이를 해결하기 위해 파일명에 해시값을 붙이거나(예: `main.1a2b3c.js`), CDN 콘솔에서 직접 캐시를 비워주는 작업이 필요하다.

### **③ 보안 강화**
많은 CDN 서비스(Cloudflare, AWS CloudFront 등)는 **DDoS 공격 방어**와 **Web Application Firewall(WAF)** 기능을 함께 제공한다. 악성 트래픽이 원본 서버에 도달하기 전에 엣지단에서 미리 차단하여 보안성을 높인다.

---

## 4. 실전 활용 예시

### **① Vercel / Next.js 정적 에셋 자동 CDN 배포**
Next.js를 Vercel에 배포하면 `public/` 디렉토리와 빌드 결과물이 자동으로 전 세계 엣지 서버에 배포된다. 별도 CDN 설정 없이 `next.config.js`의 `assetPrefix`만 지정해도 CDN URL로 에셋을 서빙할 수 있다.

```js
// next.config.js — 외부 CDN URL을 에셋 경로에 붙이는 방식
const isProd = process.env.NODE_ENV === 'production'

module.exports = {
  assetPrefix: isProd ? 'https://cdn.example.com' : '',
}

// 빌드 후 <script src> 태그가 자동으로 아래처럼 변환됨
// <script src="https://cdn.example.com/_next/static/chunks/main.js">
```

### **② Cloudflare Workers — 엣지에서 A/B 테스트 분기**
엣지 컴퓨팅의 핵심 활용 사례다. 원본 서버가 아닌 엣지에서 직접 요청을 가로채 처리하기 때문에 응답 지연이 거의 없다.

```js
// Cloudflare Worker — 사용자를 50:50으로 두 버전에 분기
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)

  // 쿠키에 실험군 정보가 없으면 랜덤 배정
  const variant = Math.random() < 0.5 ? 'A' : 'B'
  url.pathname = variant === 'A' ? '/home-v1' : '/home-v2'

  return fetch(url.toString(), request)
  // 이 모든 처리가 원본 서버가 아닌 엣지 서버에서 실행됨
}
```

### **③ CDN URL 파라미터로 이미지 최적화**
Cloudflare, ImageKit, Imgix 같은 CDN은 URL 쿼리스트링만으로 이미지 리사이징·포맷 변환을 엣지에서 처리한다. 서버에서 별도 처리 로직 없이 CDN이 자동 변환한다.

```html
<!-- 원본 이미지 -->
<img src="https://cdn.example.com/photo.jpg" />

<!-- CDN 파라미터로 크기·포맷 변환 (서버 코드 불필요) -->
<img src="https://cdn.example.com/photo.jpg?w=400&h=300&format=webp&q=80" />

<!-- Next.js의 next/image는 내부적으로 이 방식을 추상화해서 제공함 -->
<Image src="/photo.jpg" width={400} height={300} />
```

---

## 5. 기존 방식과의 비교

CDN 없이 단일 원본 서버로 모든 트래픽을 처리하는 방식과 비교한다.

```
// 기존 방식 — 모든 요청이 원본 서버 1대로 집중
사용자 (서울) ──────────────────────────► 원본 서버 (미국 버지니아)
                 왕복 약 200ms 이상
                 서버 CPU/네트워크 직접 부담

// CDN 방식 — 캐시 히트 시 엣지에서 즉시 응답
사용자 (서울) ──────► 엣지 서버 (한국) ──(캐시 히트)──► 응답
                 왕복 약 10~30ms
                 원본 서버는 캐시 만료 시에만 호출됨
```

| 비교 항목 | 단일 원본 서버 | CDN 사용 |
| :--- | :--- | :--- |
| **응답 속도** | 지리적 거리에 비례해 느림 | 가장 가까운 엣지에서 응답 |
| **원본 서버 부하** | 모든 요청 직접 처리 | 정적 콘텐츠는 엣지가 대신 처리 |
| **장애 대응** | 서버 1대 다운 = 서비스 중단 | 다른 엣지 서버가 자동 대체 |
| **비용** | 서버 스펙을 높여야 함 | CDN 트래픽 비용 발생 |
| **동적 콘텐츠** | 직접 처리 가능 | 원본 서버로 bypass 필요 |

CDN의 핵심 가치는 **정적 콘텐츠 응답을 원본 서버에서 분리**하는 데 있다. 동적 콘텐츠(API 응답, 인증 처리 등)는 여전히 원본 서버 영역이다.

---

## 6. 주의사항 및 한계

### **① 캐시 무효화는 즉각 반영되지 않는다**
엣지 서버에 캐시된 파일은 TTL(Time To Live)이 만료되기 전까지 갱신되지 않는다. 긴급 배포 후 사용자가 여전히 옛 파일을 받는 문제가 여기서 발생한다.

```js
// 잘못된 방식 — 파일명이 고정이면 캐시가 계속 유지됨
<script src="/bundle.js"></script>   // CDN이 캐시한 구버전을 계속 서빙

// 올바른 방식 — 빌드마다 해시를 파일명에 포함
<script src="/bundle.a1b2c3d4.js"></script>  // 내용이 바뀌면 파일명도 바뀜
// → CDN은 새 URL을 처음 보는 것으로 판단해 원본 서버에서 새로 가져옴
```

### **② 동적 콘텐츠 캐싱은 데이터 오염 위험이 있다**
로그인 상태, 사용자별 개인화 응답, 실시간 재고 정보 등 요청마다 달라지는 응답을 잘못 캐시하면 다른 사용자에게 노출될 수 있다.

```http
# 동적 응답에는 반드시 캐시 금지 헤더를 설정해야 함
Cache-Control: no-store, no-cache, must-revalidate

# 정적 에셋에는 장기 캐시 허용
Cache-Control: public, max-age=31536000, immutable
```

### **③ 해외 엣지 서버에 데이터가 복사된다**
CDN은 콘텐츠를 물리적으로 전 세계 서버에 복제한다. GDPR 등 개인정보 규정이 엄격한 서비스에서 개인정보가 포함된 리소스를 CDN에 올리면 규정 위반이 될 수 있다.

```
// 주의가 필요한 케이스
- 사용자 프로필 사진 (개인정보 포함 가능)
- 응답 본문에 개인정보가 포함된 API를 CDN 캐시에 저장하는 경우

// 안전한 케이스
- 공개 이미지, JS/CSS 번들, 폰트 파일 등 비개인 정적 에셋
```

**CDN은 정적 에셋 가속에는 강력하지만, 캐시 전략을 잘못 설계하면 오래된 콘텐츠 노출·데이터 오염·규정 위반 문제로 이어진다.**

