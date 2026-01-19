## 📦 Yarn vs Yarn Berry: 패키지 매니저의 진화

프론트엔드 프로젝트의 의존성 관리 방식이 `node_modules` 중심에서 효율적인 압축 및 매핑 방식으로 변화하고 있습니다.

### 1. 주요 차이점 비교

| 구분 | Yarn (Classic) | Yarn Berry (v2+) |
| --- | --- | --- |
| **버전** | v1.x 시리즈 | v2.x 이상 (완전 재설계) |
| **관리 방식** | `node_modules` 폴더 생성 | **Plug'n'Play (PnP)** 방식 |
| **의존성 위치** | 거대한 `node_modules` 트리 구조 | `.yarn/cache` (zip 압축 파일) |
| **설치 속도** | 중상 (npm보다 빠름) | **매우 빠름** (PnP 및 캐시 활용) |

### 2. 핵심 기술: Plug'n'Play (PnP)

* **Yarn:** 기존 npm과 유사하게 `node_modules`를 통해 의존성을 관리합니다. 이는 파일 개수가 너무 많아 설치가 느리고 디스크 공간을 많이 차지합니다.
* **Yarn Berry:** `node_modules`를 생성하지 않습니다. 대신 **`.pnp.cjs`** 파일을 생성하여 어떤 패키지가 어디에 위치하는지 지도를 만듭니다. 의존성은 zip 파일로 압축 보관되어 탐색 성능이 대폭 향상됩니다.

---

### 3. Zero-Install: CI/CD의 혁명

Yarn Berry의 가장 큰 장점 중 하나는 **Zero-Install** 지원입니다.

* **원리:** 모든 의존성(zip 파일)을 `.yarn/cache`에 넣고, 의존성 지도인 `.pnp.cjs`와 함께 **Git 저장소에 커밋**합니다.
* **효과:** 저장소를 Clone 받자마자 의존성이 이미 존재하므로, `yarn install` 과정 없이 바로 빌드나 테스트를 시작할 수 있습니다.

#### CI/CD 파이프라인 비교 (GitHub Actions 예시)

```yaml
# 기존 방식 (Yarn v1)
steps:
  - uses: actions/checkout@v2
  - run: yarn install  # 👈 매번 의존성을 내려받고 설치해야 함 (시간 소요)
  - run: yarn test

# Zero-Install 방식 (Yarn Berry)
steps:
  - uses: actions/checkout@v2
  - run: yarn test     # 👈 install 단계 생략 가능! 바로 실행

```