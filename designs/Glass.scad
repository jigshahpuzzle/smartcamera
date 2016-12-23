translate([0, -70, 0])
    frame();

translate([-50, -70, 0]) 
    arm1();
translate([-70, -70, 0]) 
    arm2();

module frame() {
    cube([33, 5, 3]);
    cube([5, 145, 3]);
    translate([28, 0, 0])
        cube([5, 54, 3]);
    translate([0, 60, 0])
        rotate([0, 0, -20])
            cube([33, 5, 3]);
    translate([1, 79, 0])
        rotate([0, 0, 20])
            cube([33.5, 5, 3]);
    translate([27.5, 90, 0])
        cube([5, 54, 3]);
    translate([0, 140, 0])
        cube([33, 5, 3]);
    translate([3, 4.5, 0])
        cylinder(9, 1.6, 1.6);
    translate([3, 140.5, 0])
        cylinder(9, 1.6, 1.6);
    translate([-23, 140, 0])
        cube([25, 5, 3]);
    translate([-23, 115, 0])
        cube([25, 5, 3]);
    translate([-23, 115, 0])
        cube([5, 25, 3]);
}

module arm1() {
        cube([5, 140, 3]);
        difference() {
            cube([5, 7, 8]);
                rotate([90, 0, 0])
                    translate([2.5, 5, -6])
                        cylinder(25, 2, 2);
        }
        translate([-1, 138, 0])
            rotate([0, 0, -45])
                cube([5, 22, 3]);
}

module arm2() {
        cube([5, 140, 3]);
        difference() {
            cube([5, 7, 8]);
                rotate([90, 0, 0])
                    translate([2.5, 5, -6])
                        cylinder(25, 2, 2);
        }

        translate([2, 136, 0])
            rotate([0, 0, 45])
                cube([5, 22, 3]);
}