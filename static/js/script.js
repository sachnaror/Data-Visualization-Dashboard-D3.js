async function fetchData() {
    const response = await fetch('/api/data/');
    const data = await response.json();
    // Now you have your data and can pass it to a D3.js function to visualize
    visualizeData(data);
}
fetchData();
