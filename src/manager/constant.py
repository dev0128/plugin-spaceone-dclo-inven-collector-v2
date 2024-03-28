SERVICES = {
    "aws": {
        "acm": "ACM",
        "autoscaling": "AutoScaling",
        "awslambda": "Lambda",
        "cloudformation": "CloudFormation",
        "cloudfront": "CloudFront",
        "cloudtrail": "CloudTrail",
        "cloudwatch": "CloudWatch",
        "config": "ConfigService",
        "dynamodb": "DynamoDB",
        "ec2": "EC2",
        "eks": "EKS",
        "elasticache": "ElastiCache",  #
        "elb": "ELB",
        "elbv2": "ELBv2",
        "iam": "IAM",
        "kafka": "MSK(Kafka)",  #
        "kms": "KMS",
        "rds": "RDS",
        "redshift": "Redshift",
        "s3": "S3",
        "sqs": "SQS",
        "vpc": "VPC",
        "wafv2": "WAF&Shield",  #
        "workspaces": "WorkSpaces",
    },
    "google_cloud": {
        "cloudfunction": "CloudFunctions",  #
        "cloudsql": "CloudSQL",
        "cloudstorage": "CloudStorage",  #
        "gce": "ComputeEngine",  #
        "iam": "IAM",
        "kms": "KeyManagement",
        "stackdriver": "Stackdriver",  #
    },
    "azure": {
        "AAD": "MEID(AAD)",  #
        "AppService": "AppServices",  #
        "DataBase": "DataBase",  #
        "KeyVault": "KeyVaults",  #
        "LoggingMonitoring": "Monitor",  #
        "Network": "Network",  #
        "SecurityCenter": "Security",  #
        "StorageAccounts": "StorageAccounts",  #
        "VirtualMachines": "VirtualMachines",  #
    },
}

REGION = {
    "aws": {
        "globals": "Global",
        "AllRegions": "Global",
        "global": "Global",
        "ap-northeast-1": "Asia Pacific (Tokyo)",
        "ap-northeast-2": "Asia Pacific (Seoul)",
        "ap-northeast-3": "Asia Pacific (Osaka-Local)",
        "ca-central-1": "Canada (Central)",
        "us-east-1": "US East (N. Virginia)",
        "us-east-2": "US East (Ohio)",
        "us-west-1": "US West (N. California)",
        "us-west-2": "US West (Oregon)",
        "ap-south-1": "Asia Pacific (Mumbai)",
        "ap-southeast-1": "Asia Pacific (Singapore)",
        "ap-southeast-2": "Asia Pacific (Sydney)",
        "eu-north-1": "Europe (Stockholm)",
        "eu-west-1": "Europe (Ireland)",
        "eu-west-2": "Europe (London)",
        "eu-west-3": "Europe (Paris)",
        "eu-central-1": "Europe (Frankfurt)",
        "sa-east-1": "South America (São Paulo)",
    },
    "google_cloud": {
        "globals": "Global",
        "global": "Global",
        "northamerica-northeast1": "Canada, Québec (Montréal)",
        "northamerica-northeast2": "Canada, Ontario (Toronto)",
        "us-central1": "US, Iowa (Council Bluffs)",
        "asia-east1": "Taiwan (Changhua County)",
        "asia-east2": "Hong Kong",
        "asia-northeast1": "Japan (Tokyo)",
        "asia-northeast2": "Japan (Osaka)",
        "asia-northeast3": "South Korea (Seoul)",
        "asia-south1": "India (Mumbai)",
        "asia-south2": "India (Delhi)",
        "asia-southeast1": "Singapore (Jurong West)",
        "asia-southeast2": "Indonesia (Jakarta)",
        "australia-southeast1": "Australia (Sydney)",
        "australia-southeast2": "Australia (Melbourne)",
        "europe-north1": "Finland (Hamina)",
        "europe-west1": "Belgium (St.Ghislain)",
        "europe-west2": "England, UK (London)",
        "europe-west3": "Germany (Frankfurt)",
        "europe-west4": "Netherlands (Eemshaven)",
        "europe-west6": "Switzerland (Zürich)",
        "southamerica-east1": "Brazil, São Paulo (Osasco)",
        "southamerica-west1": "Chile (Santiago)",
        "us-east1": "US, South Carolina (Moncks Corner)",
        "us-east4": "US, Northern Virginia (Ashburn)",
        "us-west1": "US, Oregon (The Dalles)",
        "us-west2": "US, California (Los Angeles)",
        "us-west3": "US, Utah (Salt Lake City)",
        "us-west4": "US, Nevada (Las Vegas)",
        "europe-southwest1": "Spain (Madrid)",
        "europe-central2": "Poland (Warsaw)",
        "africa-south1": "South Africa (Johannesburg)",
        "europe-west8": "Italy (Milan)",
        "europe-west9": "France (Paris)",
        "europe-west10": "Germany (Berlin)",
        "europe-west12": "Italy (Turin)",
        "me-central1": "Qatar (Doha)",
        "me-central2": "Saudi Arabia (Dammam)",
        "me-west1": "Israel (Tel Aviv)",
        "us-east5": "Ohio (Columbus)",
        "us-south1": "US, Texas (Dallas)",
        # "eur5": "",
    },
    "azure": {
        "globals": "Global",
        "global": "Global",
        "eastus": "(US) East US",
        "eastus2": "(US) East US 2",
        "southcentralus": "(US) South Central US",
        "westus2": "(US) West US 2",
        "westus3": "(US) West US 3",
        "australiaeast": "(Asia Pacific) Australia East",
        "southeastasia": "(Asia Pacific) Southeast Asia",
        "northeurope": "(Europe) North Europe",
        "swedencentral": "(Europe) Sweden Central",
        "uksouth": "(Europe) UK South",
        "westeurope": "(Europe) West Europe",
        "centralus": "(US) Central US",
        "southafricanorth": "(Africa) South Africa North",
        "centralindia": "(Asia Pacific) Central India",
        "eastasia": "(Asia Pacific) East Asia",
        "japaneast": "(Asia Pacific) Japan East",
        "koreacentral": "(Asia Pacific) Korea Central",
        "canadacentral": "(Canada) Canada Central",
        "francecentral": "(Europe) France Central",
        "germanywestcentral": "(Europe) Germany West Central",
        "italynorth": "(Europe) Italy North",
        "norwayeast": "(Europe) Norway East",
        "polandcentral": "(Europe) Poland Central",
        "switzerlandnorth": "(Europe) Switzerland North",
        "uaenorth": "(Middle East) UAE North",
        "brazilsouth": "(South America) Brazil South",
        "centraluseuap": "(US) Central US EUAP",
        "israelcentral": "(Middle East) Israel Central",
        "qatarcentral": "(Middle East) Qatar Central",
        "centralusstage": "(US) Central US (Stage)",
        "eastusstage": "(US) East US (Stage)",
        "eastus2stage": "(US) East US 2 (Stage)",
        "northcentralusstage": "(US) North Central US (Stage)",
        "southcentralusstage": "(US) South Central US (Stage)",
        "westusstage": "(US) West US (Stage)",
        "westus2stage": "(US) West US 2 (Stage)",
        "asia": "Asia",
        "asiapacific": "Asia Pacific",
        "australia": "Australia",
        "brazil": "Brazil",
        "canada": "Canada",
        "europe": "Europe",
        "france": "France",
        "germany": "Germany",
        "india": "India",
        "japan": "Japan",
        "korea": "Korea",
        "norway": "Norway",
        "singapore": "Singapore",
        "southafrica": "South Africa",
        "sweden": "Sweden",
        "switzerland": "Switzerland",
        "uae": "United Arab Emirates",
        "uk": "United Kingdom",
        "unitedstates": "United States",
        "unitedstateseuap": "United States EUAP",
        "eastasiastage": "(Asia Pacific) East Asia (Stage)",
        "southeastasiastage": "(Asia Pacific) Southeast Asia (Stage)",
        "brazilus": "(South America) Brazil US",
        "eastusstg": "(US) East US STG",
        "northcentralus": "(US) North Central US",
        "westus": "(US) West US",
        "japanwest": "(Asia Pacific) Japan West",
        "jioindiawest": "(Asia Pacific) Jio India West",
        "eastus2euap": "(US) East US 2 EUAP",
        "westcentralus": "(US) West Central US",
        "southafricawest": "(Africa) South Africa West",
        "australiacentral": "(Asia Pacific) Australia Central",
        "australiacentral2": "(Asia Pacific) Australia Central 2",
        "australiasoutheast": "(Asia Pacific) Australia Southeast",
        "jioindiacentral": "(Asia Pacific) Jio India Central",
        "koreasouth": "(Asia Pacific) Korea South",
        "southindia": "(Asia Pacific) South India",
        "westindia": "(Asia Pacific) West India",
        "canadaeast": "(Canada) Canada East",
        "francesouth": "(Europe) France South",
        "germanynorth": "(Europe) Germany North",
        "norwaywest": "(Europe) Norway West",
        "switzerlandwest": "(Europe) Switzerland West",
        "ukwest": "(Europe) UK West",
        "uaecentral": "(Middle East) UAE Central",
        "brazilsoutheast": "(South America) Brazil Southeast",
    },
}

METADATA_WIDGET = [
    {
        "name": "Critical",
        "type": "summary",
        "options": {"value_options": {"key": "value", "options": {"default": 0}}},
        "query": {
            "aggregate": [{"count": {"name": "value"}}],
            "filter": [
                {"key": "data.severity", "value": "CRITICAL", "operator": "eq"},
                {"key": "data.status", "value": "FAIL", "operator": "eq"},
            ],
        },
    },
    {
        "name": "High",
        "type": "summary",
        "options": {"value_options": {"key": "value", "options": {"default": 0}}},
        "query": {
            "aggregate": [{"count": {"name": "value"}}],
            "filter": [
                {"key": "data.severity", "value": "HIGH", "operator": "eq"},
                {"key": "data.status", "value": "FAIL", "operator": "eq"},
            ],
        },
    },
    {
        "name": "Low",
        "type": "summary",
        "options": {"value_options": {"key": "value", "options": {"default": 0}}},
        "query": {
            "aggregate": [{"count": {"name": "value"}}],
            "filter": [
                {"key": "data.severity", "value": "LOW", "operator": "eq"},
                {"key": "data.status", "value": "FAIL", "operator": "eq"},
            ],
        },
    },
    {
        "name": "Pass",
        "type": "summary",
        "options": {"value_options": {"key": "value", "options": {"default": 0}}},
        "query": {
            "aggregate": [{"count": {"name": "value"}}],
            "filter": [
                {"key": "data.status", "value": "PASS", "operator": "eq"},
            ],
        },
    },
    # {
    #     "name": "N/A",
    #     "type": "summary",
    #     "options": {"value_options": {"key": "value", "options": {"default": 0}}},
    #     "query": {
    #         "aggregate": [{"count": {"name": "value"}}],
    #         "filter": [
    #             {"key": "data.status", "value": "N/A", "operator": "eq"},
    #         ],
    #     },
    # },
]

ISMS = "ISMS"
ISO_27001 = "ISO-27001"
KISA_CSAP_STD = "KISA-CSAP(표준)"
KISA_CSAP_SIM = "KISA-CSAP(간편)"
PCI_DSS_4 = "PCI-DSS-4.0"
PCI_DSS_3 = "PCI-DSS-3.2.1"
CSP = "CSP 안전성 평가"
NIS_GOV = "NIS-국가-공공-기관"
NIS_PUB = "NIS-민간-기관"
NIS_SAAS = "NIS-SaaS"
D_CLO = "D-CLO-Best-Practice"

COMPLIANCE_ICON = {
    ISMS: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    ISO_27001: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    KISA_CSAP_STD: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    KISA_CSAP_SIM: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    PCI_DSS_4: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    PCI_DSS_3: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    CSP: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    NIS_GOV: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    NIS_PUB: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    NIS_SAAS: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
    D_CLO: "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/dclo/d-clo.png",
}
