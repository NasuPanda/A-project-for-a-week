resource "aws_s3_bucket" "app_bucket" {
  bucket = "media-storage-for-anki-like-app"
  acl    = "private"
  versioning {
    enabled = false # Disable versioning to save storage space
  }
  lifecycle_rule {
    id      = "expire-old-files"
    enabled = true

    expiration {
      days = 365
    }

    noncurrent_version_expiration {
      days = 90
    }
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name    = "MediaStorageForAnkiLikeApp"
    Project = "LanguageLearningApp"
    # Environment = "Production"
  }
}
