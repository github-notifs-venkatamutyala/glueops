#!/usr/bin/env python

from ensurepip import bootstrap
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_docker import Image, Container, DockerProvider
import cdktf
from imports.terraform_gcp_organization_bootstrap import TerraformGcpOrganizationBootstrap

ENVIRONMENT_NAME="test106"
ORG_ID="11111111111"
# This module can come from a registry or through a local / remote reference


class Project(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        
        



        # localModule = MyLocalModule(self, "local-module", ip_address='127.0.0.1')
        # TerraformOutput(self, "dns-server", value=localModule.dns_server_output)

        
        # cdktf.TerraformHclModule(self, "project",
                                 
        #                          source="github.com/GlueOps/terraform-gcp-organization-bootstrap.git?ref=disable-kms-protection",
        #                          variables= { 
        #                                     "gcp_billing_account_name": "My Billing Account", 
        #                                     "org_id":ORG_ID,
        #                                     "company_key": "venkat",
        #                                     "admins": ["user:venkata@example.com.com"],
        #                                     "admin_roles":[
        #                                                     "roles/owner",
        #                                                     "roles/resourcemanager.folderAdmin",
        #                                                     "roles/iam.serviceAccountUser",
        #                                                     "roles/logging.admin",
        #                                                     "roles/serviceusage.serviceUsageAdmin",
        #                                                     "roles/orgpolicy.policyAdmin",
        #                                                     "roles/servicemanagement.quotaAdmin",
        #                                                     "roles/resourcemanager.projectCreator", #added
        #                                                 ],
        #                                     "environments": [ENVIRONMENT_NAME]
        #                         }
                              
        #                          )
        output = TerraformGcpOrganizationBootstrap(self, "project", 
                                                    
                                            gcp_billing_account_name="My Billing Account", 
                                            org_id=ORG_ID,
                                            company_key="venkat",
                                            admins= ["user:venkata@example.com.com"],
                                            admin_roles=[
                                                            "roles/owner",
                                                            "roles/resourcemanager.folderAdmin",
                                                            "roles/iam.serviceAccountUser",
                                                            "roles/logging.admin",
                                                            "roles/serviceusage.serviceUsageAdmin",
                                                            "roles/orgpolicy.policyAdmin",
                                                            "roles/servicemanagement.quotaAdmin",
                                                            "roles/resourcemanager.projectCreator", #added
                                                        ],
                                        environments= [ENVIRONMENT_NAME]
                                
        
        )

        TerraformOutput(self, 'gcp_folder_id_output',
            value=output.gcp_folder_id_output
        )
        
        
        
class Vpc(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        
        cdktf.TerraformHclModule(self, "vpc",
                                 
                                 source="github.com/GlueOps/terraform-gcp-vpc-module.git?ref=feat%2Foptional-vpc-connector",
                                 variables= {
                                 "gcp_folder_id":json.load(open("test.json"))["project-test"]["gcp_folder_id_output"].split('/')[1],
                                "workspace":ENVIRONMENT_NAME,
                                "region": "us-central1",
                                "network_prefixes": {
                                          "kubernetes_pods": "10.87.0.0/16",
      "gcp_private_connect": "10.86.128.0/19",
      "kubernetes_services": "10.86.224.0/20",
      "private_primary": "10.86.0.0/23",
      "public_primary": "10.86.64.0/23",
      "serverless_vpc_connector": "10.86.96.0/28",
      "kubernetes_master_nodes": "10.86.96.16/28",
                                },
    "enable_google_vpc_access_connector": False
                                    
                                
                                }
                                 
        )
        



    







app = App()
project = Project(app, "project-test")
id = json.load(open("test.json"))["project-test"]["gcp_folder_id_output"].split('/')[1]
vpc = Vpc(app, "vpc-test",id)

Vpc.add_dependency(self=vpc, dependency= project)


app.synth()
