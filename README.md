cert-lifecycle-automation/
├── .gitignore
├── .editorconfig
├── .pre-commit-config.yaml
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitlab-ci.yml
│
├── scripts/
│   ├── check_cert.sh
│   ├── renew_cert.py
│   └── utils.py
│
├── config/
│   ├── domains.yaml
│   └── settings.yaml
│
├── tests/
│   ├── __init__.py
│   ├── test_check_cert.py
│   └── test_renew_cert.py
│
├── logs/
│   └── .gitkeep
│
├── docs/
│   ├── architecture.md
│   └── runbook.md
│
└── Makefile
