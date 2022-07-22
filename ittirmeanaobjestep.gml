if(keyboard_check(ord("W"))){
	y-=5;
	ya = -1;
}
else if(keyboard_check(ord("S"))){
	y+=5;
	ya = +1;
}
if(keyboard_check(ord("D"))){
	x+=5;
	xa = +1;
}
else if(keyboard_check(ord("A"))){
	x-=5;
	xa = -1;
}
if(keyboard_check_pressed(vk_space)){
	if(!place_meeting(x,y,obj_duvar)){
		spd = 5;
		temas = point_direction(x,y,obj_duvar.x,obj_duvar.y);
		move_towards_point(obj_duvar.x,obj_duvar.y,spd);
	}
}else if(place_meeting(x,y,obj_duvar)){
	spd=0;
	move_towards_point(x,y,0);
}
temas = point_direction(x,y,obj_duvar.x,obj_duvar.y);