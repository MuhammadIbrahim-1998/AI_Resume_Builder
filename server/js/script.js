document.getElementById("resumeInput").addEventListener("change", function () {
    const fileName = this.files.length > 0 ? this.files[0].name : "No file chosen";
    document.getElementById("fileLabel").textContent = fileName;
});

document.getElementById("resumeForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const input = document.getElementById("resumeInput");
    const file = input.files[0];
    const formData = new FormData();
    formData.append("resume", file);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result, null, 2);
});
