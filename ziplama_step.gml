y+= dikey_hiz;

if(!place_meeting(x, y+1, obj_duvar)){
	dikey_hiz += yercekimi
}
else{
	if(keyboard_check_pressed(vk_space)){
		dikey_hiz = -20;
	}
}
	
	
if(place_meeting(x, y+dikey_hiz, obj_duvar)){
	while(!place_meeting(x, y+sign(dikey_hiz), obj_duvar)){
		y += sign(dikey_hiz);
	}
	dikey_hiz = 0;
}