<?php
/*
 * 隐藏logo插件
*/

$plugins['showlogo'] = array(
		'plugin_name' => '隐藏logo',
		"enable" => 1,    			
		"edit_container" => "option_group",
		"edit_sort" => 4,
		"view_container" => "",
		"view_sort" => 1,
		"view_resource"=>1,
		"table"=>"worksmain",
  		"column"=>"hidelogo_flag"
	);


?>