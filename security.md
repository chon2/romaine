# [뉴플랫폼기술] 클라우드 보안플랫폼 개발자

## 과제 내용
- Security Group 현황을 점검하기 위해 웹기반의 AWS Security Group(이하 SG) 관리 플랫폼을 구축합니다.
- 다음 요구 사항을 만족시키는 개념 검증(Proof of Concept)을 진행한 후, 모든 산출물을 하나의 ZIP 파일로 압축하여 제출해 주세요.

## 요구사항
- SG 점검을 하기 위한  환경(Target)을 Terraform IaC로 구현합니다.
  - 3Tier 구조(dmz, app, db subnet)의 아키텍처로 구현
    - dmz sg
      - 80, 443 inbound 허용
      - dmz subnet의 t2.micro ec2에 attach
    - app sg
      - dmz web traffic만 허용
      - app subnet의 t2.micro ec2에 attach 
    - db sg
      - app traffic만 허용
      - db subnet의 tc.micro ec2에 attach
    - ssh sg
      - 22번 포트 inbound 허용
      - 어떠한 resource에도 해당 sg를 attach하지 않음
- SG 관리 플랫폼 
  - 프로그래밍 언어는 Python, Node.js, Go, Java 중 한 가지를 선택하여 웹기반으로 구현합니다.
  - AWS API를 활용 
  - REST API기반으로 구현
  - 필수 구현 기능
    - 조회
      - Security Group 전체 현황 (아래정보가 반드시 포함되어야함)
        - Aws Account Number, VPC ID, Ec2 Instance ID, Ec2 Instance Name, SG name, SG ID, SG inbound rule, SG outbound rule
      - 상기 리스트에서 개별 선택시 상세내용 조회기능
    - 추가/변경/삭제
      - SG에 inbound/outbound rule 추가/변경/삭제 기능
- 환경 구성 절차 및 개념 검증 수행 내용을 Markdown 문서로 정리합니다.

## 우대사항
- 다음중 하나 이상을 구현하는 경우
  - Security Group 참조관계 visualization 구현
  - AWS Severless or EKS 서비스를 이용하여 Security Group 관리 플랫폼 구축
  - Terraform code 모듈화 

## 기타사항
- AWS 신규 account를 생성하고 전달받은 AWS 쿠폰을 이용합니다.
  - AWS 쿠폰 사용방법
    1. 콘솔 로그인후, 우측 상단 이름에 ‘My account’ 클릭
    2. 좌측 하단에 credits 클릭
    3. Redeem credits 클릭
    4. Promotion code 및 security code 입력
    5. Redeem credits 클릭
- 과제 검수를 위한 read only 권한의 iam 계정 생성하여 id/pw 정보를 zip파일에 같이 동봉하여 제출합니다.

## 산출물
  - SG점검환경 구축을 위한 Terraform IaC 코드
  - SG관리 플랫폼 소스코드
  - 아키텍처와 usage정보가 포함된 README.md(과제 검수를 위한 read only 권한의 iam 계정정보(id/pw) 포함)
