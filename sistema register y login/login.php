include 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows == 1) {
        echo "Inicio de sesión exitoso";
    } else {
        echo "Nombre de usuario o contraseña incorrectos";
    }
}

$conn->close();
