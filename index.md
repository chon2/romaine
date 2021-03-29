
# [뉴플랫폼기술] 클라우드 개발자 - Kubernetes
## 코딩테스트 안내

### 1. 과제 내용
> 카카오뱅크에서는 Kubernetes 관리자가 클러스터에 배포되는 리소스가 허용된 형상인지 판단할 책임이 있습니다.
> 
> 다음과 같은 상황을 가정했을 때,
> 
> Kubernetes Admission Controller를 활용해 요구사항을 만족하는 로직과 배포 리소스(manifest)를 작성해주세요.
> 
> (프로그래밍 언어 제한은 없습니다.)

### 2. Presumption (상황 가정)
> 단일 kubernetes 클러스터를 사용합니다.
> 
> 어플리케이션은 Deployment resource를 통해 배포됩니다.
> 
> Deployment로 배포되는 어플리케이션 도커이미지는 kakaobank.harbor.{STAGE}만 허용합니다.
> 
> 예를들면 다음과 같습니다.

```python
if stage is dev: 
    kakaobank.harbor.dev/* 이미지만 허용  
    # ex: kakaobank.harbor.dev/nginx:latest
if stage is prod: 
    kakaobank.harbor.prod/* 이미지만 허용
    # ex: kakaobank.harbor.prod/nginx:latest
```
> stage 정보는 Deployment annotation을 통해 제공됩니다.
> 예를들면 다음과 같습니다.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: nginx
    annotations:
        stage: dev
```


### 3. Requirement (요구사항)
> 배포되는 어플리케이션 도커 이미지가 허용되는 이미지와 다를 시 다음과 같이 동작합니다.
```python
if stage is dev: 
    잘못 작성된 도커 이미지 url을 수정한다.
    """
    ex) quay.io -> kakaobank.harbor.dev
    ex) ghcr.io -> kakaobank.harbor.dev
    ex) gcr.io -> kakaobank.harbor.dev
    ex) {AWS 어카운트 ID}.dkr.ecr.{AWS 리전}.amazonaws.com -> kakaobank.harbor.dev
    """
if stage is prod: 
    배포를 허용하지 X
```
