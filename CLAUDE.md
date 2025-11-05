# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Langfuse와 multi-agent 시스템(Google ADK / A2A)을 통합하여 tracing, input-output logging, observability 파이프라인을 테스트하기 위한 실험적 플레이그라운드입니다.

## 개발 환경

- **Python 버전**: 3.13 (`.python-version` 참조)
- **가상 환경**: `.venv` (프로젝트 루트)
- **패키지 관리자**: `uv` (uv.lock 존재)
- **주요 의존성**: langfuse>=3.8.1, python-dotenv>=1.2.1
- **개발 도구**: black, mypy, ruff

## 필수 명령어

### 환경 설정
```bash
# 가상 환경 활성화
source .venv/bin/activate

# 의존성 설치
uv sync

# 환경 변수 설정 (.env 파일 생성)
cp .env.example .env
# .env 파일을 편집하여 Langfuse API 키를 설정해야 함
```

### 코드 실행
```bash
# 메인 스크립트 실행
source .venv/bin/activate && python main.py

# 예제 실행: 프롬프트 로드
source .venv/bin/activate && python examples/load_prompts.py

# 예제 실행: 프롬프트 컴파일
source .venv/bin/activate && python examples/compile_prompts.py
```

### 코드 품질 도구
```bash
# 포매팅 (black)
source .venv/bin/activate && black .

# 린트 (ruff)
source .venv/bin/activate && ruff check .

# 타입 체크 (mypy)
source .venv/bin/activate && mypy .
```

## 아키텍처

프로젝트는 Langfuse SDK를 활용한 프롬프트 관리 예제들로 구성되어 있습니다:

### 디렉토리 구조
- `main.py`: 기본 진입점 (현재 단순 출력)
- `examples/`: Langfuse 기능 예제 스크립트들
  - `load_prompts.py`: Langfuse에서 프롬프트를 가져오는 예제 (production, label, version별)
  - `compile_prompts.py`: 프롬프트 템플릿의 변수 치환(compile) 예제

### Langfuse 통합 패턴
모든 예제는 공통적으로 다음 패턴을 따릅니다:
1. `python-dotenv`로 `.env` 파일에서 환경 변수 로드
2. `initialize_langfuse()` 함수로 Langfuse 클라이언트 초기화
3. 환경 변수 검증 (LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY 필수)
4. 명확한 에러 메시지와 해결 방법 제시

### 향후 추가 예정
- **Multi-agent 시스템**: Google ADK 또는 A2A 프레임워크를 사용한 에이전트 구현
- **Tracing 파이프라인**: 에이전트 실행 추적 및 observability

## 개발 시 주의사항

### 환경 변수 관리
- `.env` 파일은 `.gitignore`에 포함되어 있으며 커밋되지 않음
- `.env.example`을 복사하여 `.env` 파일 생성 후 실제 API 키로 대체 필요
- Langfuse API 키는 https://cloud.langfuse.com의 Settings > API Keys에서 발급

### 패키지 관리
- Python 3.13을 사용하므로 최신 문법 및 기능 활용 가능
- uv 패키지 관리자를 사용하므로 의존성 추가 시 `uv add <package>` 사용
- 개발 의존성 추가 시 `uv add --dev <package>` 사용

### 코드 스타일
- Google 스타일 docstring 사용 (한국어)
- 타입 힌트 필수 (모든 public 인터페이스)
- 함수형 프로그래밍 스타일 선호 (명확한 입출력)
