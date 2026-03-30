from Loader.TLE import TleLoader
from Scheduler import SystemScheduler
from System.Interfaces import ProcessorInterface
from System import SpaceSystem
from System.Modules.Navigation import SpacecraftNavigation

# -----------------------------------------------
# Load Data
# -----------------------------------------------
filename = r'C:\Users\Adam\Documents\Repos\DataPlotter\Loader\TLE\SampleData\20260322_starlink_tle.txt'
loader = TleLoader(filename)
loader.load_data()
all_states = loader.get_astro_state()

# using one state for now
state = all_states[0]
# -----------------------------------------------
# System and Subsystems
# -----------------------------------------------
# create the overall system
spacecraft = SpaceSystem(state.name)
spacecraft.print_name()
# create all associated TRUTH subsystems
# and attach them to the system
truth_navigator = SpacecraftNavigation()
truth_navigator.set_state(state.r, state.v)
spacecraft.truth.push(truth_navigator)
# create all associated HARDWARE subsystems
# and attach them to the system
# -----nothing here yet-----
# create all associated SOFTWARE subsystems
# and attach them to the system
navigator = SpacecraftNavigation()
navigator.set_state(state.r, state.v)
spacecraft.software.push(navigator)

# create the processor interfce container
systemProcessor = ProcessorInterface()
systemProcessor.set_system(spacecraft)
systemProcessor.set_valid()

# -----------------------------------------------
# Scheduler and associated objects
# -----------------------------------------------
# create scheduler
scheduler = SystemScheduler()
scheduler.set_max_time(50.0)
scheduler.set_time_step(0.01)

scheduler.push(systemProcessor)

# -----------------------------------------------
# Execute code and run assessment
# -----------------------------------------------
scheduler.run()