# pangshon

FaaS Functions with Railpack

- BuildKit + railpack are used to build and run function images from folders like `template-python`.

Quick start

- Install Docker and ensure it’s running
- Install railpack: `curl -fsSL https://raw.githubusercontent.com/railwayapp/railpack/main/install.sh | bash`

Common commands

- Build: `./build template-python`
  - Options: `--name my-image`, `--platform linux/amd64|linux/arm64`, `--progress auto|plain|tty`
- Run server only (auto port): `./run template-python`
  - 지정 포트 사용: `./run template-python 8080`
- Run + POST JSON (auto port 기본):
  - `./run template-python --json '{"name":"world","good_name":"alice"}'`
  - or `./run template-python --json-file payload.json`
- Push: `./push template-python ghcr.io/<you> v0.1.0`

Testing

- 단일 케이스 테스트:
  - `./test template-python tests/payload.json`
  - 상태코드만 확인(기본 200). 커스텀: `--status 201`
  - 본문 포함 검사: `--contains hello`
  - 경로/메서드 지정: `--path / --method POST`
  - 컨테이너 유지: `--keep`

예시 payload 파일 내용 (`tests/payload.json`):

```
{"name":"world","good_name":"alice"}
```

Notes

- The scripts auto-start a local BuildKit daemon in Docker and set `BUILDKIT_HOST=docker-container://buildkit` for you.
- `template-python/main.py` expects JSON `{"name": "...", "good_name": "..."}` on POST `/`.
