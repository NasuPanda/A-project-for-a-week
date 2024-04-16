resource "aws_instance" "app_server" {
  # Tokyo, Ubuntu, 20.04 LTS, amd64 focal image build on 2024-02-28
  # https://cloud-images.ubuntu.com/locator/ec2/
  ami           = "ami-0db548937a54fa3a7"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "ApplicationServer"
  }
}
