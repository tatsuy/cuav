#error "error, including dc1394.h"
#include <dc1394/dc1394.h>

#define chameleon_t dc1394_t 
#define chameleon_camera_t dc1394camera_t
#define chameleon_frame_t dc1394video_frame_t
#define chameleon_camera_reset dc1394_camera_reset

#define chameleon_video_set_transmission dc1394_video_set_transmission
#define chameleon_video_set_iso_speed dc1394_video_set_iso_speed
#define chameleon_video_set_mode dc1394_video_set_mode
#define chameleon_video_set_framerate dc1394_video_set_framerate
#define chameleon_capture_setup dc1394_capture_setup
#define chameleon_feature_set_power dc1394_feature_set_power
#define chameleon_feature_set_mode dc1394_feature_set_mode
#define chameleon_feature_set_value dc1394_feature_set_value
#define chameleon_feature_get_value dc1394_feature_get_value
#define chameleon_feature_set_absolute_control dc1394_feature_set_absolute_control
#define chameleon_feature_set_absolute_value dc1394_feature_set_absolute_value
#define chameleon_set_control_register dc1394_set_control_register
#define chameleon_get_control_register dc1394_get_control_register
#define chameleon_capture_stop dc1394_capture_stop
#define chameleon_camera_free dc1394_camera_free
#define chameleon_free dc1394_free
#define chameleon_new dc1394_new
#define chameleon_camera_new dc1394_camera_new
#define chameleon_capture_enqueue dc1394_capture_enqueue
#define chameleon_capture_dequeue dc1394_capture_dequeue
#define chameleon_camera_read dc1394_camera_read
#define chameleon_drain_queue(c, t)

