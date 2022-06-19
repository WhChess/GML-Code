image_angle = point_direction(x,y,mouse_x,mouse_y);
if(spd==0){
	move_towards_point(x,y,spd);
}
if(h=0){
	if(mouse_check_button_pressed(mb_left)){
		h=1;
		instance_create_layer(mouse_x,mouse_y,"Instances",obj_main2);
		spd = 5;
		move_towards_point(mouse_x,mouse_y,spd);
	}
}
if(place_meeting(x,y,obj_main2)){
		a = 1;
}