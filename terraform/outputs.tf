
output "application_name" {
  description = "Name of the application"
  value       = terraform_data.task_manager.output.application
}

output "environment" {
  description = "Application environment"
  value       = terraform_data.task_manager.output.environment
}

output "platform" {
  description = "Infrastructure platform"
  value       = terraform_data.task_manager.output.platform
}

output "resource_id" {
  description = "Terraform resource identifier"
  value       = terraform_data.task_manager.id
}
