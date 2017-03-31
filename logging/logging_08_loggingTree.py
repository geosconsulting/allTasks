import otherMod2
import logging
import logging_tree

log = logging.getLogger('')

class main():

    logging.info("Program started")
    result = otherMod2.add(7, 8)
    logging.info("Done!")

    logging_tree.printout()

    def index(self):
        log.error('Test message')
        return 'Hello world!'
    index.exposed = True

if __name__ == '__main__':
    main()