FROM ubuntu:20.04

ENV REGISTRATION_TOKEN=GR1348941DaJZamQKP2A9MCy5xP4C

RUN apt-get update && \
    apt-get install -y curl git && \
    curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash && \
    apt-get install -y gitlab-runner

RUN gitlab-runner register \
  --non-interactive \
  --executor "docker" \
  --docker-image alpine:latest \
  --url https://gitlab.informatika.org/ \
  --registration-token $REGISTRATION_TOKEN \
  --description "docker runner for rpl k02 g08" \
  --maintenance-note "rebuild docker runner if failed" \
  --tag-list docker-runner-rpl-g08 \
  --run-untagged="true" \
  --locked="true" \
  --access-level="not_protected"

CMD ["gitlab-runner", "run"]