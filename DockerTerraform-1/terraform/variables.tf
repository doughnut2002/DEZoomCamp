variable "credentials" {
  description = "My Credentials"
  default     = "./Keys/terraform-keys.json"
}

variable "location" {
  description = "My location"
  default     = "EU"
}

variable "region" {
  description = "My Region"
  default     = "us-central1"
}

variable "bq_dataset_name" {
  description = "Bigquery Dataset name"
  default     = "de_dataset"
}

variable "gcs_storage_class" {
  description = "GCS storage class name"
  default     = "Standard"

}

variable "gcs_bucket_name" {
  description = "GCS storage bucket name"
  default     = "shekharsproject-terra-bucket"
}
variable "project" {
  description = "Project name"
  default     = "gothic-sylph-387906"
}