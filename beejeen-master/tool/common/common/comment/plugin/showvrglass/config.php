<?php
/*
 * vr切换插件
*/

$plugins['showvrglass'] = array(
		'plugin_name' => 'VR切换',
		"enable" => 1,    			
		"edit_container" => "option_group",
		"edit_sort" => 6,
		"view_container" => "right_top",
		"view_sort" => 1,
		"view_resource"=>1,
		"table"=>"worksmain",
  		"column"=>"hidevrglasses_flag"
	);

?>