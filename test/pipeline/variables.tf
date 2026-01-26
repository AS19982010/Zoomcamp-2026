variable "credentials" {
  description = "My Credentials"
  default     = "moj-klucz.json" # <--- WPISZ NAZWĘ SWOJEGO PLIKU JSON
}

variable "project" {
  description = "Project"
  default     = "twoje-id-projektu" # <--- WPISZ SWOJE PROJECT ID Z GCP
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "twoje-id-projektu-terra-bucket" # <--- MUSI BYĆ UNIKALNA NA ŚWIECIE
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}