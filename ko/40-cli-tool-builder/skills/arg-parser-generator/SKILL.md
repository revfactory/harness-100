---
name: arg-parser-generator
description: "CLI 도구의 인자 파서 구조를 체계적으로 설계하고 코드를 생성하는 방법론. 'CLI 인자 설계', '옵션 구조', '서브커맨드 설계', '인자 파서 생성', '도움말 설계' 등 CLI 인자 체계 설계 시 사용한다. 단, GUI 인터페이스 설계, TUI 프레임워크 통합은 이 스킬의 범위가 아니다."
---

# Arg Parser Generator — CLI 인자 파서 설계 + 코드 생성

command-designer와 core-developer의 인자 파서 설계를 강화하는 스킬.

## 대상 에이전트

- **command-designer** — 명령 체계와 옵션 구조를 설계한다
- **core-developer** — 인자 파서 코드를 구현한다

## CLI 인자 유형 분류

| 유형 | 형식 | 예시 |
|------|------|------|
| 위치 인자 | `<arg>` | `convert input.json` |
| 필수 옵션 | `--name VALUE` | `--output out.yaml` |
| 선택 옵션 | `[--name VALUE]` | `[--indent 2]` |
| 플래그 | `[--flag]` | `[--verbose]` |
| 다중 값 | `--name V1 V2` | `--files a.txt b.txt` |
| 열거형 | `--type {a,b,c}` | `--format {json,yaml}` |
| 환경변수 | `$ENV_VAR` | `$API_KEY` |

## 서브커맨드 설계 패턴

### 패턴 1: 동사형 (CRUD)

```
mytool create <resource> [options]
mytool list [resource] [--filter]
mytool get <id> [--format]
mytool update <id> [options]
mytool delete <id> [--force]
```

### 패턴 2: 리소스형 (kubectl 스타일)

```
mytool user list
mytool user create --name "name"
mytool project deploy --env prod
```

### 패턴 3: 파이프라인형 (Unix 철학)

```
mytool parse input.json | mytool transform --schema s.yaml | mytool output
```

## 옵션 네이밍 규칙

```
1. 짧은/긴 옵션 쌍: -o / --output
2. 불리언 + 부정: --color / --no-color
3. 일관된 명사: --output-dir (동사 X → --write-to X)
4. 축약 가능: --config → --cfg (혼동 없을 때)

금지 패턴:
- -h (help 예약), -V (version 예약)
- 대문자 단축옵션 (-A, -B) — 혼동 유발
- 너무 긴 옵션 (--output-directory-path)
```

## 언어별 파서 라이브러리 + 보일러플레이트

### Python (typer — 권장)

```python
import typer
from typing import Optional
from enum import Enum

app = typer.Typer(help="파일 변환 CLI")

class Format(str, Enum):
    json = "json"
    yaml = "yaml"
    toml = "toml"

@app.command()
def convert(
    input_file: str = typer.Argument(..., help="입력 파일"),
    from_format: Format = typer.Option(..., "--from", "-f", help="입력 형식"),
    to_format: Format = typer.Option(..., "--to", "-t", help="출력 형식"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="출력 파일"),
    indent: int = typer.Option(2, "--indent", help="들여쓰기"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="상세 로그"),
):
    """파일 형식을 변환합니다."""
    ...

if __name__ == "__main__":
    app()
```

### Node.js (commander)

```javascript
const { Command } = require('commander');
const program = new Command();

program
  .name('mytool')
  .description('파일 변환 CLI')
  .version('1.0.0');

program
  .command('convert <input>')
  .option('-f, --from <format>', '입력 형식', 'json')
  .option('-t, --to <format>', '출력 형식', 'yaml')
  .option('-o, --output <file>', '출력 파일')
  .action((input, options) => { ... });

program.parse();
```

### Go (cobra)

```go
var convertCmd = &cobra.Command{
    Use:   "convert [input]",
    Short: "파일 형식 변환",
    Args:  cobra.ExactArgs(1),
    RunE: func(cmd *cobra.Command, args []string) error {
        from, _ := cmd.Flags().GetString("from")
        to, _ := cmd.Flags().GetString("to")
        // ...
        return nil
    },
}

func init() {
    convertCmd.Flags().StringP("from", "f", "json", "입력 형식")
    convertCmd.Flags().StringP("to", "t", "yaml", "출력 형식")
    convertCmd.Flags().StringP("output", "o", "", "출력 파일")
}
```

## 도움말 출력 표준

```
Usage: mytool <command> [options]

Commands:
  convert    파일 형식 변환
  validate   파일 유효성 검사
  diff       두 파일 비교

Options:
  -h, --help       도움말 표시
  -V, --version    버전 표시
  -v, --verbose    상세 출력
  --no-color       색상 비활성화

Examples:
  mytool convert input.json --to yaml
  mytool validate schema.json data.json

Environment:
  MYTOOL_CONFIG    설정 파일 경로
```

## 종료 코드 표준

| 코드 | 의미 | 사용 |
|------|------|------|
| 0 | 성공 | 정상 완료 |
| 1 | 일반 오류 | 실행 중 오류 |
| 2 | 인자 오류 | 잘못된 인자/옵션 |
| 126 | 권한 없음 | 파일 접근 불가 |
| 127 | 의존성 없음 | 필요한 도구 미설치 |
| 130 | 사용자 중단 | Ctrl+C |
