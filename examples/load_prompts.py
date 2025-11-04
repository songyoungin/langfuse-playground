"""Langfuse에서 프롬프트를 가져오는 예제 코드입니다.

이 스크립트는 다음 기능을 제공합니다:
- 최신 프로덕션 프롬프트 가져오기
- 특정 버전의 프롬프트 가져오기
- 특정 레이블의 프롬프트 가져오기
- 프롬프트 변수 치환 (컴파일)

실행 방법:
    source .venv/bin/activate && python examples/load_prompts.py

환경 변수 설정:
    .env 파일에 다음 환경 변수를 설정해야 합니다:
    - LANGFUSE_PUBLIC_KEY: Langfuse 프로젝트의 공개 키
    - LANGFUSE_SECRET_KEY: Langfuse 프로젝트의 비밀 키
    - LANGFUSE_HOST (선택사항): Langfuse 호스트 URL
"""

import os
from typing import Any, Dict, Optional

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


def fetch_prompt_latest(langfuse: Langfuse, prompt_name: str) -> Any:
    """최신 프로덕션 프롬프트를 가져옵니다.

    Args:
        langfuse: Langfuse 클라이언트
        prompt_name: 가져올 프롬프트의 이름

    Returns:
        프롬프트 클라이언트 객체
    """
    print(f"\n{'='*80}")
    print(f"[예제 1] 최신 프로덕션 프롬프트 가져오기: {prompt_name}")
    print(f"{'='*80}")

    prompt = langfuse.get_prompt(name=prompt_name)

    print(f"\n프롬프트 이름: {prompt.name}")
    print(f"버전: {prompt.version}")
    print(f"Config: {prompt.config}")
    print(f"\n템플릿 내용:")
    print(f"{'-'*80}")
    print(prompt.prompt)
    print(f"{'-'*80}")

    return prompt


def fetch_prompt_by_version(
    langfuse: Langfuse, prompt_name: str, version: int
) -> Any:
    """특정 버전의 프롬프트를 가져옵니다.

    Args:
        langfuse: Langfuse 클라이언트
        prompt_name: 가져올 프롬프트의 이름
        version: 가져올 프롬프트의 버전 번호

    Returns:
        프롬프트 클라이언트 객체
    """
    print(f"\n{'='*80}")
    print(f"[예제 2] 특정 버전 프롬프트 가져오기: {prompt_name} (버전 {version})")
    print(f"{'='*80}")

    prompt = langfuse.get_prompt(name=prompt_name, version=version)

    print(f"\n프롬프트 이름: {prompt.name}")
    print(f"버전: {prompt.version}")
    print(f"Config: {prompt.config}")
    print(f"\n템플릿 내용:")
    print(f"{'-'*80}")
    print(prompt.prompt)
    print(f"{'-'*80}")

    return prompt


def fetch_prompt_by_label(
    langfuse: Langfuse, prompt_name: str, label: str
) -> Any:
    """특정 레이블의 프롬프트를 가져옵니다.

    Args:
        langfuse: Langfuse 클라이언트
        prompt_name: 가져올 프롬프트의 이름
        label: 가져올 프롬프트의 레이블 (예: "production", "latest")

    Returns:
        프롬프트 클라이언트 객체
    """
    print(f"\n{'='*80}")
    print(f"[예제 3] 특정 레이블 프롬프트 가져오기: {prompt_name} (레이블: {label})")
    print(f"{'='*80}")

    prompt = langfuse.get_prompt(name=prompt_name, label=label)

    print(f"\n프롬프트 이름: {prompt.name}")
    print(f"버전: {prompt.version}")
    print(f"레이블: {label}")
    print(f"Config: {prompt.config}")
    print(f"\n템플릿 내용:")
    print(f"{'-'*80}")
    print(prompt.prompt)
    print(f"{'-'*80}")

    return prompt


def compile_prompt_example(
    prompt: Any, variables: Optional[Dict[str, Any]] = None
) -> str:
    """프롬프트 변수를 치환(컴파일)하는 예제입니다.

    Args:
        prompt: 프롬프트 클라이언트 객체
        variables: 치환할 변수 딕셔너리

    Returns:
        변수가 치환된 프롬프트 문자열
    """
    print(f"\n{'='*80}")
    print("[예제 4] 프롬프트 변수 치환 (컴파일)")
    print(f"{'='*80}")

    if variables is None:
        variables = {}

    print(f"\n입력 변수: {variables}")

    compiled = prompt.compile(**variables)

    print(f"\n치환 결과:")
    print(f"{'-'*80}")
    print(compiled)
    print(f"{'-'*80}")

    return compiled


def main() -> None:
    """메인 함수입니다.

    Langfuse 프롬프트 가져오기의 다양한 예제를 실행합니다.
    """
    try:
        # 1. Langfuse 클라이언트 초기화
        print("Langfuse 클라이언트 초기화 중...")
        langfuse = initialize_langfuse()
        print("✓ Langfuse 클라이언트가 성공적으로 초기화되었습니다.")

        # 예제를 실행하기 위해서는 Langfuse 대시보드에서 프롬프트를 생성해야 합니다.
        # 아래는 'example-prompt'라는 이름의 프롬프트가 존재한다고 가정한 예제입니다.

        # 2. 최신 프로덕션 프롬프트 가져오기
        # prompt = fetch_prompt_latest(langfuse, "example-prompt")

        # 3. 특정 버전 프롬프트 가져오기
        # prompt_v1 = fetch_prompt_by_version(langfuse, "example-prompt", version=1)

        # 4. 특정 레이블 프롬프트 가져오기
        # prompt_production = fetch_prompt_by_label(
        #     langfuse, "example-prompt", label="production"
        # )

        # 5. 프롬프트 컴파일 (변수 치환)
        # 프롬프트에 {{name}}과 같은 변수가 있다면 다음과 같이 치환할 수 있습니다:
        # compile_prompt_example(prompt, {"name": "세레나", "topic": "AI"})

        print("\n" + "=" * 80)
        print("예제 실행 완료!")
        print("=" * 80)
        print("\n주의: 실제로 프롬프트를 가져오려면 Langfuse 대시보드에서")
        print("프롬프트를 먼저 생성하고, 위의 주석 처리된 코드를 활성화하세요.")
        print("\n프롬프트 생성 방법:")
        print("1. https://cloud.langfuse.com 에 로그인")
        print("2. 프로젝트 선택")
        print("3. Prompts 메뉴에서 새 프롬프트 생성")
        print("4. 프롬프트 이름을 'example-prompt'로 설정하거나")
        print("   코드에서 프롬프트 이름을 실제 이름으로 변경")

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
