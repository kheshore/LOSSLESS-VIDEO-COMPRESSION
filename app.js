const form = document.getElementById('upload-form');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById('mp4-file').files[0];
  const formData = new FormData();
  formData.append('mp4-file', fileInput.files[0]);

  fetch('/convert', {
    method: 'POST',
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    
    result.innerHTML = `<a href="${data.hevc_file}">Download mkv File</a>`;
  });
});
