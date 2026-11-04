variable "application_name" {
  description = "Name of the application"
  type        = string
  default     = "Task Manager"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "development"
}

variable "platform" {
  description = "Infrastructure platform"
  type        = string
  default     = "local"
}
