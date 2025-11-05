"""Langfuse 프롬프트 템플릿을 컴파일(변수 치환)하는 예제 코드입니다.

prompt.compile()을 사용하여 프롬프트 템플릿의 변수를 실제 값으로 치환합니다.
- 프롬프트 가져오기
- 변수 치환 (compile)
- 여러 변수 세트로 컴파일 예제

실행 방법:
    source .venv/bin/activate && python examples/compile_prompts.py

환경 변수 설정:
    .env 파일에 다음 환경 변수를 설정해야 합니다:
    - LANGFUSE_PUBLIC_KEY: Langfuse 프로젝트의 공개 키
    - LANGFUSE_SECRET_KEY: Langfuse 프로젝트의 비밀 키
    - LANGFUSE_HOST (선택사항): Langfuse 호스트 URL

Langfuse 대시보드에서 추천 프롬프트 템플릿:
    1. 채팅 어시스턴트:
       You are a helpful AI assistant named {{assistant_name}}.
       User {{user_name}} asks: {{question}}
       Please provide a detailed answer in {{language}}.

    2. 코드 리뷰:
       Review the following {{language}} code:
       {{code}}

       Provide feedback on:
       - Code quality
       - Potential bugs
       - Best practices

    3. 텍스트 요약:
       Summarize the following text in {{max_length}} words:
       {{text}}

    4. 번역:
       Translate the following text from {{source_lang}} to {{target_lang}}:
       {{text}}

    5. 감정 분석:
       Analyze the sentiment of the following text.
       Categories: {{categories}}
       Text: {{text}}
"""

import os
from typing import Any, Dict

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

    프롬프트를 가져와서 다양한 변수로 컴파일하는 예제를 실행합니다.
    """
    try:
        # Langfuse 클라이언트 초기화
        print("Langfuse 클라이언트 초기화 중...")
        langfuse = initialize_langfuse()
        print("✓ Langfuse 클라이언트가 성공적으로 초기화되었습니다.\n")

        prompt_name = "langfuse-playground/compile-example"

        # 프롬프트 가져오기
        print("=" * 80)
        print(f"프롬프트 가져오기: {prompt_name}")
        print("=" * 80)

        prompt = langfuse.get_prompt(name=prompt_name)

        print(f"\n프롬프트 이름: {prompt.name}")
        print(f"버전: {prompt.version}")
        print("\n원본 템플릿:")
        print("-" * 80)
        print(prompt.prompt)
        print("-" * 80)

        # 예제 1: 기본 변수 치환
        print("\n" + "=" * 80)
        print("[예제 1] 기본 변수 치환")
        print("=" * 80)

        variables_1: Dict[str, Any] = {
            "assistant_name": "Claude",
            "user_name": "세레나",
            "question": "Langfuse의 프롬프트 관리 기능에 대해 설명해주세요.",
            "language": "한국어",
        }

        print("\n입력 변수:")
        for key, value in variables_1.items():
            print(f"  {key}: {value}")

        compiled_1 = prompt.compile(**variables_1)

        print("\n컴파일 결과:")
        print("-" * 80)
        print(compiled_1)
        print("-" * 80)

        # 예제 2: 다른 변수 세트로 컴파일
        print("\n" + "=" * 80)
        print("[예제 2] 다른 변수 세트로 컴파일")
        print("=" * 80)

        variables_2: Dict[str, Any] = {
            "assistant_name": "AI Helper",
            "user_name": "개발자",
            "question": "Python에서 비동기 프로그래밍을 어떻게 시작하나요?",
            "language": "English",
        }

        print("\n입력 변수:")
        for key, value in variables_2.items():
            print(f"  {key}: {value}")

        compiled_2 = prompt.compile(**variables_2)

        print("\n컴파일 결과:")
        print("-" * 80)
        print(compiled_2)
        print("-" * 80)

        # 예제 3: 부분 변수 치환 (일부 변수만 제공)
        print("\n" + "=" * 80)
        print("[예제 3] 부분 변수 치환 시도")
        print("=" * 80)

        variables_3: Dict[str, Any] = {
            "user_name": "테스터",
            "question": "변수가 부족하면 어떻게 되나요?",
        }

        print("\n입력 변수 (일부만 제공):")
        for key, value in variables_3.items():
            print(f"  {key}: {value}")

        try:
            compiled_3 = prompt.compile(**variables_3)
            print("\n컴파일 결과:")
            print("-" * 80)
            print(compiled_3)
            print("-" * 80)
        except Exception as e:
            print(f"\n✗ 컴파일 실패: {e}")
            print(f"오류 타입: {type(e).__name__}")
            print("\n참고: 모든 템플릿 변수에 값을 제공해야 합니다.")

        print("\n" + "=" * 80)
        print("예제 실행 완료!")
        print("=" * 80)
        print("\n💡 프롬프트 템플릿 작성 팁:")
        print("1. 변수는 {{variable_name}} 형식으로 작성")
        print("2. 변수명은 명확하고 설명적으로 작성")
        print("3. 모든 변수에 대한 기본값 또는 검증 로직 고려")
        print("4. Langfuse 대시보드에서 프롬프트 버전 관리 활용")

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
        print("\n참고: Langfuse 대시보드에서 프롬프트가 생성되어 있는지 확인하세요.")


if __name__ == "__main__":
    main()
