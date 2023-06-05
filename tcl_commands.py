COMMIT;    # Commits the current transaction, making all the changes permanent.
ROLLBACK;  # Rolls back the current transaction, undoing all the changes since the last commit.
SAVEPOINT savepoint_name;  # Sets a savepoint within the current transaction, allowing a partial rollback to that point if needed.
RELEASE SAVEPOINT savepoint_name; # Releases a previously set savepoint, making the changes up to that point permanent.
ROLLBACK TO SAVEPOINT savepoint_name;  # Rolls back the transaction to a previously set savepoint, undoing the changes made after that savepoint.
SET TRANSACTION isolation_level;   # Sets the transaction characteristics such as isolation level or transaction access mode.


 



