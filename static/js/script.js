function signin() {
    let username = document.getElementById('name').value;
    let password = document.getElementById('password').value;
    
    let url = '/dashboard?username=' + username + '&password=' + password;
    window.open(url, '_self');
}

function show_settings(id) {
    document.getElementById(id).style.display = "flex";
}

function hide_settings(id) {
    document.getElementById(id).style.display = "none";
}

function update_funds(name, id, new_funds_id) {
    let new_funds = document.getElementById(new_funds_id).value;
    fetch('/edit-fund?name=' + name + '&id=' + id + '&new_funds=' + new_funds)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // Parse response as JSON
      })
      .then(data => {
        window.alert(data); // Handle the response data
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });

    location.reload();
}

function delete_bank(id) {
    fetch('/delete-bank?id=' + id)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // Parse response as JSON
      })
      .then(data => {
        window.alert(data); // Handle the response data
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });

    location.reload();
}

function new_bank() {
    let name = document.getElementById("popup-name").value;
    let funds = document.getElementById("popup-funds").value;
    let url = '/new-bank?name=' + name + '&funds=' + funds;

    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // Parse response as JSON
      })
      .then(data => {
        window.alert(data); // Handle the response data
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });

    location.reload();

}

function show_popup() {
    document.getElementById("popup").style.display = "flex";
}

function hide_popup() {
    document.getElementById("popup").style.display = "none";
}
