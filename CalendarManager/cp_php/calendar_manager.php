<!DOCTYPE html>
<!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->
<!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->
<!--[if !IE]><!--> <html lang="en"> <!--<![endif]-->
<head>
    <title>Calendar Manager</title>
    <?php include "cp_php/header.php"; ?>
</head>

<body>
    <?php include "cp_php/navbar.php"; ?>

		<div class="container sections-wrapper">
			<div class="row">
				<div class="primary col-md-12 col-sm-12 col-xs-12">
					<section class="section">
						<div class="section-inner">
							<h2 class='heading'>Calendar Manager</h2>
							<div class="form-group">
								<form class="formValidation form-group" action="calendar.php" method="post">
									Month:
									<input name="date" type="month"/>
									<input type="submit"/>
									</br>
								</form>
							</div>
						</div>
					</section>
				</div>
			</div>
		</div>

</body>
</html>
