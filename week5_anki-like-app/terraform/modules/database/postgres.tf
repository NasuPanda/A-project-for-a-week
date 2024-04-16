# Free tier /w RDS: https://aws.amazon.com/rds/free/

# Variables
variable "db_password" {
  description = "db password"
  type        = string
}

resource "aws_db_instance" "postgres" {
  identifier = "appdb"
  allocated_storage    = 20
  instance_class       = "db.t3.micro"
  engine               = "postgres"
  engine_version       = "12"
  username             = "appuser"
  password             = var.db_password
  db_subnet_group_name = aws_db_subnet_group.db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.db_sg.id]

  tags = {
    Name = "ApplicationDatabase"
  }
}

resource "aws_db_subnet_group" "db_subnet_group" {
  name       = "main-db-subnet-group"
  subnet_ids = [aws_subnet.public.id]

  tags = {
    Name = "MainDBSubnetGroup"
  }
}

resource "aws_security_group" "db_sg" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
}
