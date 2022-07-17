import data_analysis
import gui
import weather
import tianqi


def main():
    weather.write_csv(gui.text_city)
    tianqi.main(gui.text_city, gui.text_time)
    data_analysis.main()