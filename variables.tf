variable "name" {
  description = "Your Spotify playlist name"
  type        = string
}

variable "description" {
  description = "Your Spotify playlist description"
  type        = string
}

variable "keywords" {
  description = "A list of keywords to search for songs"
  type        = list(string)
}
