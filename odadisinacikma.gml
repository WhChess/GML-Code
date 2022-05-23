if(keyboard_check(ord("W"))){
	y-=5;
}
else if(keyboard_check(ord("S"))){
	y+=5;
}
if(keyboard_check(ord("D"))){
	x+=5;
}
else if(keyboard_check(ord("A"))){
	x-=5;
}
x=clamp(x, 0+sprite_xoffset, room_width-sprite_xoffset);
y=clamp(y, 0+sprite_yoffset, room_height-sprite_yoffset);
