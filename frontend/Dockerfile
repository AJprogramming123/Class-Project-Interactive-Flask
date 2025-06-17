# Use lightweight nginx image
FROM nginx:alpine

# Remove default HTML files
RUN rm -rf /usr/share/nginx/html/*

# Copy static files (CSS, JS, etc.)
COPY ./static /usr/share/nginx/html/static

# Copy HTML files (e.g., index.html)
COPY ./templates /usr/share/nginx/html

# Expose port 80 for serving
EXPOSE 80
