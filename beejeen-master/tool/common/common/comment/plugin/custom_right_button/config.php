<?php
/*
 * 自定义右键菜单
*/

$plugins['custom_right_button'] = array(
		'plugin_name' => '自定义右键菜单',
		"enable" => 1,    			
		"edit_container" => "setting_group",
		"edit_sort" => 6,
		"edit_resource"=>1,
		"view_container" => "",
		"view_sort" => 2,
		"view_resource"=>1,
		"xml" => 'plugin.xml.php'
	);


?>