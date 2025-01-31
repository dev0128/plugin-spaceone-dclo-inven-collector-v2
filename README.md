# spaceOne - Plugin V2 로컬 세팅

### 기본 구조

- 클라이언트에서 D-CLO Plugin을 설치하고
- 수집 REST API를 통해, D-CLO Engine에서 결과를 받음

![D-CLO plugin 구조](/aws.png)

### 개발 환경 세팅

- 아래와 같이 개발 환경 세팅
- python : `3.10.*`
- vscode

### python 의존성 설치

- poetry 사용
- 또는 `requriments.txt` 파일 사용

```python
$ poetry install
```

#### gRPC 서버 환경 초기화

1. `spacectl_config.yaml` 파일 세팅 후

2. init 명령어 사용해서 적용

```python
$ spacectl config init -f yaml/spacectl_config.yaml

> local
```

### 서버 환경 확인

- `init` 명령 후 제대로 세팅되었는지 확인

```python
$ spacectl config show
```

### 로컬 플러그인 gRPC 서버 구동

- vscode 디버깅 세팅
- `F5` 디버깅으로 gRPC 서버 실행
- `.vscdoe/launch.json` 파일 작성

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "spaceOne Plugin",
            "type": "debugpy",
            "request": "launch",
            "module": "spaceone.core.command",
            "args": [
                "run",
                "plugin-server",
                "src"
            ],
            "justMyCode": false,
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "python": "${command:python.interpreterPath}"
        }
    ]
}
```

- 또는 가상환경에서 아래 명령어 입력

```python
$ python -m spaceone.core.command run plugin-server src
```

### 로컬 플러그인 gRPC 서버 요청

- 서버에 요청
- 각 프로바이더 yaml 파일 작성 후
  - ⚠️ 실제 키 정보가 커밋되지 않게 주의
  - ctl 폴더로 yaml 복사해서 작성 후 사용
- spacectl exec 사용하여 데이터 수집

```python
$ mkdir -p ctl

$ spacectl exec collect inventory.Collector -f ./ctl/aws.yaml
```
