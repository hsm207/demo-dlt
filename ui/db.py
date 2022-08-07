from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import Session, registry

engine = create_engine("postgresql://admin:admin@db:5432/demo", future=True, echo=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    sentiment = Column(String)
    confidence = Column(Float)

    def __repr__(self):
        return f"id: {self.id}\ntext: {self.text}\nsentiment: {self.sentiment}\nconfidence: {self.confidence}\n"


mapper_registry.metadata.create_all(engine)

msg1 = Message(text="I am so happy")
msg2 = Message(text="I am so sad")
msg3 = Message(text="I am fine")

msgs = [msg1, msg2, msg3]

with Session(engine) as session:
    session.add_all(msgs)
    session.commit()
