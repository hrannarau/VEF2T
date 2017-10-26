<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h2>SIGN UP</h2>
	<form action="/send" method="post">
		<div>
			<label>Create Username</label><br>
			<input type="text" placeholder="Enter Username" name="username">
			<br>
			<label>Create Password</label><br>
			<input type="password" placeholder="Enter Password" name="password" minlength="4" maxlength="20">
			<br><br>
			<div>
				<button type="submit" class="signupbtn">Sign Up</button>
			</div>
		</div>
	</form>
</body>
</html>