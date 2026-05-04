function getData() {
    fetch('/api/data')
        .then(res => res.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
        });
}