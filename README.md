# insta-doc-pic

## Specs

### Script

- Get unique link from backend
  - Generate QR code from link
- Give instructions to user
- Every minute, call backend for images
  - Insert images into cursor position

### Backend
- Generate a unique link from Google Doc instance call
  - Will link to page with big upload button for user uploaded photos
- Receive photos and store in database associated with unique instance
- Receive call from script for photos in database
  - Delete photos after sending
