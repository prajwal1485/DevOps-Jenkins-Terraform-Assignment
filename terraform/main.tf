# Local Terraform resource for Task Manager

resource "terraform_data" "task_manager" {
  input = {
    application = var.application_name
    environment = var.environment
    platform    = var.platform
    version     = "1.0"
  }
}
