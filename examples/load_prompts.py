"""Langfuse에서 프롬프트를 가져오는 예제 코드입니다.

langfuse.get_prompt()를 사용하여 다양한 방식으로 프롬프트를 가져옵니다:
- Production 프롬프트 가져오기 (default)
- 특정 label의 프롬프트 가져오기
- 특정 version의 프롬프트 가져오기

실행 방법:
    source .venv/bin/activate && python examples/load_prompts.py

환경 변수 설정:
    .env 파일에 다음 환경 변수를 설정해야 합니다:
    - LANGFUSE_PUBLIC_KEY: Langfuse 프로젝트의 공개 키
    - LANGFUSE_SECRET_KEY: Langfuse 프로젝트의 비밀 키
    - LANGFUSE_HOST (선택사항): Langfuse 호스트 URL
"""

import os
from typing import Dict

from dotenv import load_dotenv
from langfuse import Langfuse

# 환경 변수 로드
load_dotenv()


def initialize_langfuse() -> Langfuse:
    """Langfuse 클라이언트를 초기화합니다.

    환경 변수에서 API 키를 읽어 Langfuse 클라이언트를 생성합니다.

    Returns:
        초기화된 Langfuse 클라이언트

    Raises:
        ValueError: 필수 환경 변수가 설정되지 않은 경우
    """
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST")

    if not public_key or not secret_key:
        raise ValueError(
            "LANGFUSE_PUBLIC_KEY와 LANGFUSE_SECRET_KEY 환경 변수가 설정되어야 합니다. "
            ".env 파일을 확인하세요."
        )

    langfuse_kwargs: Dict[str, str] = {
        "public_key": public_key,
        "secret_key": secret_key,
    }

    if host:
        langfuse_kwargs["host"] = host

    return Langfuse(**langfuse_kwargs)


def main() -> None:
    """메인 함수입니다.

    langfuse.get_prompt()를 사용하여 다양한 방식으로 프롬프트를 가져오는 예제를 실행합니다.
    """
    try:
        # Langfuse 클라이언트 초기화
        print("Langfuse 클라이언트 초기화 중...")
        langfuse = initialize_langfuse()
        print("✓ Langfuse 클라이언트가 성공적으로 초기화되었습니다.\n")

        prompt_name = "langfuse-playground/example"

        # 1. Production 프롬프트 가져오기 (default)
        print("=" * 80)
        print(f"[예제 1] Production 프롬프트 가져오기: {prompt_name}")
        print("=" * 80)

        prompt_production = langfuse.get_prompt(name=prompt_name)

        print(f"\n프롬프트 이름: {prompt_production.name}")
        print(f"버전: {prompt_production.version}")
        print(f"Config: {prompt_production.config}")
        print("\n템플릿 내용:")
        print("-" * 80)
        print(prompt_production.prompt)
        print("-" * 80)

        # 2. 특정 레이블의 프롬프트 가져오기
        print("\n" + "=" * 80)
        print(f"[예제 2] 레이블 지정 프롬프트 가져오기: {prompt_name} (label: 251105)")
        print("=" * 80)

        prompt_label = langfuse.get_prompt(name=prompt_name, label="251105")

        print(f"\n프롬프트 이름: {prompt_label.name}")
        print(f"버전: {prompt_label.version}")
        print("레이블: 251105")
        print(f"Config: {prompt_label.config}")
        print("\n템플릿 내용:")
        print("-" * 80)
        print(prompt_label.prompt)
        print("-" * 80)

        # 3. 특정 버전의 프롬프트 가져오기
        print("\n" + "=" * 80)
        print(f"[예제 3] 버전 지정 프롬프트 가져오기: {prompt_name} (version: 1)")
        print("=" * 80)

        prompt_version = langfuse.get_prompt(name=prompt_name, version=1)

        print(f"\n프롬프트 이름: {prompt_version.name}")
        print(f"버전: {prompt_version.version}")
        print(f"Config: {prompt_version.config}")
        print("\n템플릿 내용:")
        print("-" * 80)
        print(prompt_version.prompt)
        print("-" * 80)

        print("\n" + "=" * 80)
        print("예제 실행 완료!")
        print("=" * 80)

    except ValueError as e:
        print(f"✗ 오류: {e}")
        print("\n해결 방법:")
        print("1. 프로젝트 루트에 .env 파일을 생성하세요.")
        print("2. .env.example 파일을 참고하여 API 키를 설정하세요.")
        print("3. Langfuse 대시보드 (https://cloud.langfuse.com)에서")
        print("   Settings > API Keys 메뉴에서 API 키를 발급받을 수 있습니다.")
    except Exception as e:
        print(f"✗ 예상치 못한 오류가 발생했습니다: {e}")
        print(f"오류 타입: {type(e).__name__}")


if __name__ == "__main__":
    main()
