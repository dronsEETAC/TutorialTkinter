import json
import tkinter as tk
import tkintermapview

class MapFrameClass:

    def buildFrame(self, fatherFrame):
        self.fatherFrame = fatherFrame
        self.MapFrame = tk.Frame(fatherFrame)
        self.planning = False
        self.button1 = tk.Button(self.MapFrame, width=10, text="Start", bg='green', fg="white", command=self.start)
        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2 = tk.Button(self.MapFrame, width=10, text="Finish", bg='red', fg="white", command=self.finish)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3 = tk.Button(self.MapFrame, width=10, text="Clear", bg='blue', fg="white", command=self.clear)
        self.button3.grid(row=0, column=2, padx=5, pady=5)
        self.map_widget = tkintermapview.TkinterMapView(self.MapFrame, width=800, height=600, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan = 2, padx=5, pady=5)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map_widget.set_position(41.275946, 1.987475)
        self.map_widget.set_zoom(20)
        #self.map_widget.add_left_click_map_command(self.left_click_event)
        self.map_widget.add_right_click_menu_command(label="Insert WP",
                                                command=self.add_marker_event,
                                                pass_coords=True)



        return self.MapFrame

    '''def left_click_event (self, position):
        print ('Position left click ', position)'''

    def add_marker_event (self, position):
        if self.planning:
            self.count = self.count + 1
            marker = self.map_widget.set_marker(position[0],position[1], text= self.count )

            if self.count > 1:
                path = self.map_widget.set_path([self.positions[-1],position], color = 'red')
                self.paths.append(path)

            self.positions.append(position)
            self.markers.append(marker)

    def start (self):
        self.planning = True
        self.count = 0
        self.positions = []
        self.markers = []
        self.paths = []



    def finish (self):
        self.planning = False
        path = self.map_widget.set_path(self.positions, color='green')
        self.paths.append(path)


    def clear (self):
        print ('celar')
        self.count = 0
        self.positions = []
        for marker in self.markers:
            marker.delete ()
        self.markers = []
        for path in self.paths:
            path.delete ()
        self.paths = []
