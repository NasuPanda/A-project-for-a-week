resource "aws_dynamodb_table" "user_sessions" {
  name           = "UserSessions"
  billing_mode   = "PROVISIONED"  # provisioned mode for Free Tier benefits
  hash_key       = "session_id"

  attribute {
    name = "session_id"
    type = "S"
  }

  attribute {
    name = "user_id"
    type = "S"
  }

  read_capacity_units  = 1  # Minimize read and write capacity to fit Free Tier
  write_capacity_units = 1

  tags = {
    Purpose = "ManageUserSessions"
  }
}
