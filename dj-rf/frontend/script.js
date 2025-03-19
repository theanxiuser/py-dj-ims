document.addEventListener("DOMContentLoaded", () => {
    const root = document.getElementById("root");

    fetch("http://localhost:8000/api/blogs")
        .then(response => response.json())
        .then(data => {
            data.forEach(blog => {
                const blogDiv = document.createElement("div");
                blogDiv.className = "blog";
                blogDiv.innerHTML = `
                    <h2>${blog.title}</h2>
                    <p>${blog.content}</p>
                    <p>Status: ${blog.status}</p>
                `;
                root.appendChild(blogDiv);
            });
        })
        .catch(error => {
            console.error(error);
        })
})