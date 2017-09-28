<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h2>SIGN UP</h2>
	<form action="/send" method="post">
		<div>
			<label>Name</label><br>
			<input type="text" placeholder="Enter Name" name="name">
			<br>
			<label>Create Username</label><br>
			<input type="text" placeholder="Enter Username" name="username">
			<br>
			<label>Create Password</label><br>
			<input type="password" placeholder="Enter Password" name="password" minlength="4" maxlength="20">
			<br>
			<label>Telephone Number</label><br>
			<input type="text" placeholder="Enter Telephone" name="number" pattern="[0-9]{7}">
			<br>
			<label>Email Address</label><br>
			<input type="email" placeholder="Enter Email Address" name="email">
			<div>
				<button type="submit" class="signupbtn">Sign Up</button>
			</div>
		</div>
	</form>
</body>
</html>