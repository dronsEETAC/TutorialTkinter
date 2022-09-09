import tkinter as tk


class ParameterFrameClass:

    def buildFrame(self, fatherFrame):
        self.fatherFrame =fatherFrame
        self.ParameterFrame = tk.Frame(fatherFrame)
        self.closeButton = tk.Button(self.ParameterFrame, text="Close", bg='red', fg="white",
                                     command=self.closeButtonClicked)
        self.closeButton.pack()


        return self.ParameterFrame

    def closeButtonClicked (self):
        self.fatherFrame.destroy()

