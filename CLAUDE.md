# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Langfuse와 multi-agent 시스템(Google ADK / A2A)을 통합하여 tracing, input-output logging, observability 파이프라인을 테스트하기 위한 실험적 플레이그라운드입니다.

## 개발 환경

- **Python 버전**: 3.14 (`.python-version` 참조)
- **가상 환경**: `.venv` (프로젝트 루트)
- **패키지 관리자**: `uv` (uv.lock 존재)
- **주요 의존성**: langfuse>=3.8.1
- **개발 도구**: black, mypy, ruff

## 필수 명령어

### 환경 설정
```bash
# 가상 환경 활성화
source .venv/bin/activate

# 의존성 설치
uv sync
```

### 코드 실행
```bash
# 메인 스크립트 실행
source .venv/bin/activate && python main.py
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

현재 프로젝트는 초기 설정 단계이며, main.py에 기본 진입점만 구현되어 있습니다. 향후 다음 컴포넌트들이 추가될 예정입니다:

- **Langfuse 통합**: tracing과 observability를 위한 Langfuse SDK 통합
- **Multi-agent 시스템**: Google ADK 또는 A2A 프레임워크를 사용한 에이전트 구현
- **로깅 파이프라인**: input-output 로깅 및 추적 메커니즘

## 개발 시 주의사항

- Python 3.14를 사용하므로 최신 문법 및 기능 활용 가능
- uv 패키지 관리자를 사용하므로 의존성 추가 시 `uv add <package>` 사용
- 개발 의존성 추가 시 `uv add --dev <package>` 사용
